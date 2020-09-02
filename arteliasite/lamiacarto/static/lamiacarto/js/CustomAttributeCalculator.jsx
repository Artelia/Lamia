/**
 * Copyright 2017, Sourcepole AG.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */

function customAttributeCalculator(layer, feature) {
    // Here you can dynamically return additional attribute values for the
    // identify dialog, possibly depending on the passed layer and feature.
    // Return a list of <tr> elements i.e.:
    //
    //   return [(
    //       <tr key="custom-attr">
    //           <td className="identify-attr-title"><i>Name</i></td>
    //           <td className="identify-attr-value">Value</td>
    //       </tr>
    //   )];
    return [];
}

module.exports = customAttributeCalculator;
