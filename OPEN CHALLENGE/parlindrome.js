// PARLINDROME WITH REDUCE HELPER

 function pal (str) {
     return str === [...str].reduce((previous, current) => current + previous, '');
 }

 console.log(pal('abba'))
