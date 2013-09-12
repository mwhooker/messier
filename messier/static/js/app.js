"use strict";

angular.module("Messier", ["messier.services.ec2", "messier.services.stack", "messier.filters.ec2", "messier.filters.stack", "messier.filters.util"])
               .config(["$routeProvider", "$locationProvider",
                        function($routeProvider, $locationProvider) {
                            $routeProvider
                                .when("/", {
                                    templateUrl: "/static/partials/home.html",
                                    controller: IndexController
                                })
                                .when("/ec2/instances", {
                                    templateUrl: "/static/partials/ec2/instances.html",
                                    controller: EC2Controller
                                })
                                .when("/stacks", {
                                    templateUrl: "/static/partials/stacks.html",
                                    controller: StackController
                                })
                                .otherwise({
                                    redirectTo: "/"
                                });

                            $locationProvider.html5Mode(true);
                        }]);
