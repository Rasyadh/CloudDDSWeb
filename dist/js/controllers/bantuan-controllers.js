var app = angular.module('bantuan-controllers', []);

app.controller('InfobantuanController', function(){
    this.bInfo = infoContent;
});

var infoContent = [
    {
        image: "assets/images/question.png",
        title: "FAQ",
        description: "Frequently asked questions."
    },
    {
        image: "assets/images/customer-service.png",
        title: "Customer Service",
        description: "Layanan customer service 24 jam."
    }
];