// header
var h1 = document.getElementById("plone");
var h2 = document.getElementById("pltwo");
var h3 = document.getElementById("playto");

// buttons
var b1 = document.getElementById("pluno");
var b2 = document.getElementById("pluto");
var reset = document.getElementById("reset");

// limit
var inputRange = document.getElementById("limit");
// var winningLimit = parseInt(inputRange.value);

var clickedOne = 0;
var clickedTwo = 0;
var isOver = false;
var winningLimit = 0;
// var limit = winningLimit;

b1.addEventListener("click",function()
    {
         if(!isOver)
         {
           clickedOne++;
           if(clickedOne === winningLimit)
           {
            isOver = true;
            h1.classList.add("changeClr");
           }
           h1.textContent = clickedOne;
         }
    });

b2.addEventListener("click",function()
    {
         if(!isOver)
         {
           clickedTwo++;
           if(clickedTwo === winningLimit)
           {
            isOver = true;
            h2.classList.add("changeClr");
           }
           h2.textContent = clickedTwo;
         }
    });

reset.addEventListener("click",function()
   {
        resettt();
   });

function resettt()
{
        clickedOne = 0;
        clickedTwo = 0;
        isOver = false;
        // inputRange = 0;
        h1.textContent = 0;
        h2.textContent = 0;
        h1.classList.remove("changeClr");
        h2.classList.remove("changeClr");
}

inputRange.addEventListener("change", function()
   {
       h3.textContent = inputRange.value;
       winningLimit = Number(inputRange.value);
       resettt();
   });
