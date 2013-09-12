"use strict";

if (typeof String.prototype.endsWith != "function") {
    String.prototype.endsWith = function(str) {
        return this.slice(-str.length) == str;
    };
}

angular.module("messier.filters.ec2", [])
    .filter("launch_timestamp", function() {
        return function(timestamp) {
            return new Date(Date.parse(timestamp)).toUTCString();
        };
    })
    .filter("instance_status", function($filter) {
        return function(status) {
            if (status == "running") {
                return "<span class='label label-success'>"+status+"</span>";
            } else {
                return "<span class='label label-danger'>"+status+"</span>";
            }
        };
    })
    .filter("hostname_or_ipaddress", function($filter) {
        return function(instance) {
            if (instance.dns_name) {
                return instance.dns_name;
            } else {
                return instance.ip_address;
            }
        };
    })
    .filter("json_pretty_print", function() {
        return function(json) {
            return JSON.stringify(json, undefined, 4);
        };
    })
    .filter("groups_formatted", function() {
        return function(groups) {
            var groupList = [];
            for (var group in groups) {
                if (groups.hasOwnProperty(group)) {
                    groupList.push(groups[group].name);
                }
            }
            return groupList.join(", ");
        };
    });

angular.module("messier.filters.stack", [])
    .filter("stack_status", function($filter) {
        return function(status) {
            if (status == "CREATE_IN_PROGRESS") {
                return "<span class='label label-info'><i class='icon-refresh icon-spin'></i> "+$filter("lowercase")(status)+"</span>";
            } else if (status == "DELETE_IN_PROGRESS") {
                return "<span class='label label-default'><i class='icon-refresh icon-spin'></i> "+$filter("lowercase")(status)+"</span>";
            } else if (status.endsWith("_FAILED")) {
                 return "<span class='label label-danger'>"+$filter("lowercase")(status)+"</span>";
            }
            return ""
        };
    });

angular.module("messier.filters.util", [])
    .filter("unix_timestamp_date", function() {
        return function(timestamp) {
            return new Date(timestamp*1000).toUTCString();
        };
    });
