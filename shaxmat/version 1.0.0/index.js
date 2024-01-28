
const box = document.getElementsByClassName("example-box");
const box_ches = document.getElementsByClassName("ches-selection");
var box_width = 8;
var box_height = 8;
var t = document.getElementById("ches-board");
var a = document.createElement("span");


var end_id = 0;
var select_ches = 'pawn';
var images = { 'pawn': 'chess-pawn.png', 'rook': 'chess-rook.png', 'knight': 'chess-knight.png', 'bishop': 'chess-bishop.png', 'queen': 'chess-queen.png', 'king': 'chess-king.png' };
/*
0 - > pawn
1 - > rook
2 - > knight
3 - > bishop
4 - > queen
5 - > king
*/
function setBgColor(id) {
    box[id].style.backgroundColor = "rgb(255, 100,0)";
    box[id].classList.add("active-box");
    box[id].style.backgroundImage = "url('icons/" + images[select_ches];
    // console.log("icons/"+images[select_ches]+id);
}

function draw_bg_color(i, j) {
    let temp = i * box_width + j;
    // console.log(temp);
    box[temp].style.backgroundColor = "black";
}

function functionClick(event) {
    // console.log(event.srcElement.id);
    // setBgColor(event.srcElement.id);
    // rowChek(event.srcElement.id);
    var id = event.srcElement.id;
    deleteActive();
    end_id = event.srcElement.id;
    box[id].classList.add("ches-active");
    switch (select_ches) {
        case 'pawn': pawn(id); break;
        case 'rook': rook(id); break;
        case 'knight': knight(id); break;
        case 'bishop': bishop(id); break;
        case 'queen': queen(id); break;
        case 'king': king(id); break;
        default: console.log('ERROR NOT SELECTED');
    }
}
function functionClickSelection(event) {
    document.getElementById(select_ches).classList.remove("active-ches");
    select_ches = event.srcElement.id;
    var element = document.getElementById(select_ches).classList.add("active-ches");
    console.log(select_ches);
}
function setNavbarClick() {
    box_ches[0].addEventListener("click", functionClickSelection);
    box_ches[0].setAttribute("id", 'pawn');
    box_ches[1].addEventListener("click", functionClickSelection);
    box_ches[1].setAttribute("id", 'rook');
    box_ches[2].addEventListener("click", functionClickSelection);
    box_ches[2].setAttribute("id", 'knight');
    box_ches[3].addEventListener("click", functionClickSelection);
    box_ches[3].setAttribute("id", 'bishop');
    box_ches[4].addEventListener("click", functionClickSelection);
    box_ches[4].setAttribute("id", 'queen');
    box_ches[5].addEventListener("click", functionClickSelection);
    box_ches[5].setAttribute("id", 'king');
}

function setFunctionClick() {
    for (var i = 0; i < box.length; i++) {
        box[i].addEventListener("click", functionClick);
        box[i].setAttribute("id", i);
        // box[i].;
    }
    setNavbarClick();
}
/* ustunni tekshirish */
function columnChek(id) {
    var i = Math.floor(id / box_width);
    var j = id % box_width;
    /* yuqoriga */
    while (i >= 0) {
        let temp = i * box_width + j;
        setBgColor(temp);
        i--;
        // console.log(temp);
    }
    i = Math.floor(id / box_width) + 1;
    j = id % box_width;
    /* pastga */
    while (i < box_height) {
        let temp = i * box_width + j;
        setBgColor(temp);
        i++;
        // console.log(temp);
    }
}
/* qatorni tekshirish */
function rowChek(id) {
    var i = Math.floor(id / box_width);
    var j = id % box_width;
    while (j >= 0) {
        let temp = i * box_width + j;
        setBgColor(temp);
        j--;
        // console.log(temp);
    }
    i = Math.floor(id / box_width);
    j = id % box_width + 1;
    while (j < box_width) {
        let temp = i * box_width + j;
        setBgColor(temp);
        j++;
        // console.log(temp);
    }

}

function diganal1(id) {
    var i = Math.floor(id / box_width);
    var j = id % box_width;
    while (i >= 0 && j >= 0) {
        let temp = i * box_width + j;
        setBgColor(temp);
        i--; j--;
        // console.log(temp);
    }
    i = Math.floor(id / box_width) + 1;
    j = id % box_width + 1;
    while (i < box_height && j < box_width) {
        let temp = i * box_width + j;
        setBgColor(temp);
        i++; j++;
        // console.log(temp);
    }
}
function diganal2(id) {
    var i = Math.floor(id / box_width);
    var j = id % box_width;
    while (i >= 0 && j < box_width) {
        let temp = i * box_width + j;
        setBgColor(temp);
        i--; j++;
        // console.log(temp);
    }
    i = Math.floor(id / box_width) + 1;
    j = id % box_width - 1;
    while (i < box_height && j >= 0) {
        let temp = i * box_width + j;
        setBgColor(temp);
        i++; j--;
        // console.log(temp);
    }
}

function deleteActive() {
    box[end_id].classList.remove("ches-active");
    for (var i = 0; i < box.length; i++) {
        box[i].classList.remove("active-box");
        box[i].style.backgroundColor = "red";
        box[i].style.backgroundImage = null;
        box[i].style.animation = "both";
    }
}
function pawn(id) {
    var i = Math.floor(id / box_width);
    setBgColor(id);
    i--;
    if(i>=0){
        setBgColor(id-box_width);
    }
}
function rook(id) {
    columnChek(id);
    rowChek(id);
}
function bishop(id) {
    diganal1(id);
    diganal2(id);
}
function knight(id) {
    /* 1 usul */
    var x = Math.floor(id / box_width);
    var y = id % box_width;
    setBgColor(id);
    for(var i=0;i<box_height;i++){
        for(var j=0;j<box_width;j++){
            if(Math.pow(x-i,2)+Math.pow(y-j,2)==5){
                setBgColor(i*box_width+j);
            }
        }
    }
    /* 2 usul */
    // for(var i=x-2;i<=x+2;i++){
    //     for(var j=y-2;j<=y+2;j++){
    //         if(Math.pow(x-i,2)+Math.pow(y-j,2)==5){
    //             setBgColor(i*box_width+j);
    //         }
    //     }
    // }
}
function queen(id) {
    columnChek(id);
    rowChek(id);
    diganal1(id);
    diganal2(id);
}
function king(id) {
    var x = Math.floor(id / box_width);
    var y = id % box_width;
    setBgColor(id);
    for(var i=x-1;i<=x+1;i++){
        for(var j=y-1;j<=y+1;j++){
            if(i>=0 && j>=0 && i<box_height && j<box_width){
                setBgColor(i*box_width+j);
            }
        }
    }
}

setFunctionClick();
