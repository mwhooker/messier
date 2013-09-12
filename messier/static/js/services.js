"use strict";

angular.module("messier.services.ec2", ["ngResource"])
    .factory("EC2Instances", function($resource) {
        return {
            list: $resource("/ec2/instances.json", {page: 1}, {
                query: {
                    method: "GET"
                }
            }),
            get: $resource("/ec2/instances/:instanceId.json", {}, {
                query: {
                    method: "GET",
                    params: {instanceId: "@instanceId"},
                    isArray: false
                }
            })
        }
    });

angular.module("messier.services.stack", ["ngResource"])
    .factory("Stacks", function($resource) {
        return {
            list: $resource("/stacks.json", {}, {
                query: {
                    method: "GET",
                    params: {},
                    isArray: true
                }
            }),
            delete: $resource("/stacks/:stackId.json", {}, {
                query: {
                    method: "DELETE",
                    params: {stackId: "@stackId"},
                }
            })
        }
    });
