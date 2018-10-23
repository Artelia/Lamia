import os

from json import JSONDecoder, JSONEncoder

from .document import Document


class Cipher(object):

    def encrypt(self, nonce, data, associated_data):
        raise NotImplementedError('Subclasses should implement this!')

    def decrypt(self, nonce, data, associated_data):
        raise NotImplementedError('Subclasses should implement this!')


from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class AESGCM(Cipher):

    def __init__(self, key):
        self._aesgcm = AESGCM(key)

    def _generate_nonce(self):
        return os.urandom(12)

    def encrypt(self, data):
        return self._aesgcm.encrypt(self._generate_nonce(), data, None)

    def decode(self, data):



class EncryptedDocument(Document):

    def __init__(self, cipher, database, document_id, encrypted_keys=None):

        class EncryptEncoder(JSONEncoder):

            def encode(self, o):
                for k in encrypted_keys:
                    if k in o:
                        o[k] = cipher.encode(o[k])

                return super(EncryptEncoder, self).encode(o)

        class DecryptDecoder(JSONDecoder):

            def decode(self, s, **kwargs):
                data = super(DecryptDecoder, self).decode(s, **kwargs)

                for k in encrypted_keys:
                    if k in data:
                        data[k] = cipher.decode(data[k])

                return data

        super(EncryptedDocument, self).__init__(
            database,
            document_id=document_id,
            encoder=EncryptEncoder,
            decoder=DecryptDecoder
        )

    @classmethod
    def from_doc(cls, doc, encrypted_keys=None):
        if not isinstance(doc, Document):
            raise Exception('Not type Document!')

        new_doc = cls(doc._database,
                      document_id=doc._document_id,
                      encrypted_keys=encrypted_keys)
        new_doc.update(doc.json())

        return new_doc

    @classmethod
    def from_dict(cls, d, database, encrypted_keys=None):
        if not isinstance(d, dict):
            raise Exception('Not type dict!')

        new_doc = cls(database,
                      document_id=d.get('_id', None),
                      encrypted_keys=encrypted_keys)
        new_doc.update(d)

        return new_doc