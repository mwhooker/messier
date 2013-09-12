"use strict";

function IndexController($scope) {
}

function EC2Controller($scope, $parse, $location, EC2Instances) {
    $scope.getInstances = function(page) {
        var rsp = EC2Instances.list.query({page: page}, function() {
            if (rsp["items"].length > 0) {
                $scope.instances = rsp["items"];
                $scope.currentPage = page;
                $scope.numPages = rsp["pages"];
                $scope.pages = [{
                    num: page-1,
                    name: "«",
                    cls: page == 1 ? "disabled" : ""
                }]

                for (var i = 1; i <= rsp["pages"]; i++) {
                    $scope.pages.push({
                        num: i,
                        name: i,
                        cls: page == i ? "active" : ""
                    });
                }

                $scope.pages.push({
                    num: page+1,
                    name: "»",
                    cls: page == rsp["pages"] ? "disabled" : ""
                });
            }
        });
    };

    $scope.showDetails = function(instance) {
        if ($("#footer").css("display") == "none") {
            $scope.instance = instance;
            $("#footer").show();
        } else {
            if ($scope.instance == instance) {
                $("#footer").hide();
            } else {
                $scope.instance = instance;
            }
        }
    };
}

function StackController($scope, $location, Stacks) {
    var self = this;
    $scope.stacks = Stacks.list.query();
    $scope.deleteStack = function(stack) {
        Stacks.delete.query({stackId: stack.stack_id});
        $scope.stacks = Stacks.list.query();
    };

    self.refreshStacks = function() {
        $scope.stacks = Stacks.list.query();

        setTimeout(self.refreshStacks, 10000);
    };

    self.refreshStacks();
}
