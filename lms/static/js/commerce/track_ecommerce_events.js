/**
 *
 * A library of helper functions to track ecommerce related events. 
 *
 */

(function(define) {
    'use strict';

    define([
        'jquery',
    ], function($) {
        trackUpsellClick = function(linkName, optionalAttrs) {
            if (!window.analytics) {
                return;
            }
    
            var eventAttrs = { "linkName": linkName };

            if (
                typeof optionalAttrs !== 'undefined' &&
                optionalAttrs !== null &&
                Object.keys(optionalAttrs).length > 0
            ) {
                var allowedAttrs = ["courseId", "pageName"];
                allowedAttrs.map(
                    allowedAttr => eventAttrs[allowedAttr] = optionalAttrs[allowedAttr]
                );
            }
    
            window.analytics.track("edx.bi.ecommerce.upsell_links_clicked", eventAttrs);
        };
        
        TrackECommerceEvents = {
            trackUpsellClick: trackUpsellClick,
        };

        return TrackECommerceEvents;
    });
}).call(this, define || RequireJS.define);