.. toctree::
    :maxdepth: 2

Creating a database
#################################

Understanding global logic
*****************************

To adapt Lamia to a particular thematic, all the work is done within the Lamia.config module.

The first thing to do is to  create a new module in Lamia.config, eg 'wowthematic'

Here create a submodule named 'dbase'. HEre are all datas for :

* creating the dbase structure

* all CRUD (Creation/Read/Update/Delete) action with the dbase.


1 - The dbase structure is in a .ods (libreoffice) file, here named wowthematic_0_0.ods

The first part of name must be the same as the global module name.
Then, the two integers will be used to version the database : if you want to modify////update the dbase, create a file named wowthematic_0_1.ods
and Lamia will add new tables and columns in the database.

2. The CRUD actions are in a file named dbasetest_0_0_crud.py
this file is used for all Creation/Read/Update/Delete action for Lamia.
Basic xx_crud.py file can be found in Lamia.config.base3.dbase.base3_crud.py.

The .ods file
****************

Each table are in a new tab of the spreadsheet. 
The tab name must be [number]_[tablename]. The number is important because tables will be created respecting this number order.

The tab has a minimal structure :

TODO

Reserved tablename
======================
[something]data is a name for data table. It's linked to a parent table by a lpk_[tablename] column.


Reserved column name
=====================

pk_ is for the column of the primary key

id_  is for the column of the identifant of the row

lpk_[tablename]  is for foreign key column to the table [tablename]

lid_[tablename] is for link to the table [tablename]


The _crud.py file
******************

The minimal class is here :

.. code-block:: python

    from Lamia.api.dbasemanager.dbaseparserabstract import AbstractDBaseParser
    from Lamia.config.base3.dbase.base3_crud import LamiaORM as BaseLamiaORM


    class LamiaORM(BaseLamiaORM):
        def __init__(self, dbase):
            super().__init__(dbase)


You can implement crud operations like this :


.. code-block:: python

    class TopologicLamiaORM(BaseLamiaORM):
        def __init__(self, dbase):
            super().__init__(dbase)

        class Node(BaseLamiaORM.AbstractTableOrm):
            def create(self, featurepk=None):
                super().create(featurepk)
                [...]

            def read(self, pk):
                [...]

            def update(self, pk, valuesdict):
                super().update(pk, valuesdict)
                [...]

            def delete(self, pk):
                super().delete(pk)
                 [...]


The name of the class must be the name of the Table titled.


            


