var Paper = 0;
var num_idx = 0;
var display_paper = 0;
var P_Per_Second = 0;
var t = new Date();
var last_t = new Date();
var upgrades_amount = [0,0];
var upgrades_price = [10,0];
var upgrades_inflation = [1.1, 0]
var upgrades_max = [100000000,0]
var upgrades_name = ['Auto Clicker','???']
var number_names = [""," Thousand"," Million", " Billion", " Trillion", " Quadrillion", " Quintillion", " Sextillion", " Septillion", " Octillion"]
function ClickCounter(Amount) {

    Paper = Paper + Amount;
    updateCounter()
}

function updateCounter() {
    document.getElementById("count").innerHTML = shrinkNumber(Paper) + " Paper";
    document.getElementById("autoAmount").innerHTML = P_Per_Second;
}

function subAuto(Amount) {
    P_Per_Second -= Amount;
    updateCounter()
}

function addAuto(Amount) {
    P_Per_Second += Amount;
    updateCounter()
}

function AddClicks() {
    Paper = Paper + (P_Per_Second * ((t - last_t) / 1000));
}


setInterval(GameTick,1);

function GameTick() {
    P_Per_Second = upgrades_amount[0];
    t = new Date();
    AddClicks();
    updateCounter();
    last_t = t;

}

function shrinkNumber(number) {
    var num_idx = 0;
    var num = number;
    while(num > 1000){
        num = num / 1000;
        num_idx += 1;
    }

    if(num_idx > 0){
        num = Math.floor(num * 100)/100;
    } else {
        num = Math.floor(num);
    }

    num = num + number_names[num_idx];
    
    return num;
}

function Upgrades(id, div_id) {

    if (Paper > upgrades_price[id] && upgrades_amount < upgrades_max) {
        Paper = Paper - upgrades_price[id];
        upgrades_amount[id] += 1;
        updateCounter();
    }
    document.getElementById(div_id).innerHTML = upgrades_name[id] + ": " + upgrades_price[id];


}