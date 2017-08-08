
var application = angular.module('mainApp', []) ;

application.controller('mainController', function($scope, fromService, fromFactory, fromProvider){

        $scope.generateRandom = function(){
        $scope.serviceNumber = fromService.generates();
        $scope.factoryNumber = fromFactory.generatef();
        $scope.providerMessage = fromProvider.showDate();
        
    };
});

application.service('fromService', function(){   //SERVICE
    
    this.generates = function (){
        return Math.random()*10;
    };
});

application.factory('fromFactory', function(){  //FACTORY
        var factoryObject = {};
        factoryObject.generatef = function(){
        return Math.random()*10;
        };
        return factoryObject;
});

application.provider('fromProvider', function(){   //PROVIDER
        var msg ;
        return{
            setmsg : function(value){
                msg = value; 
            },
            $get : function(){    //injection
                return{
                    showDate: function(){
                        var date = new Date();
                        return date.getHours();
                    }
                }
            }
        }
});


