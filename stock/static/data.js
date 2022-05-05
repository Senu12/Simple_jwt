// var data = {
//     "status": true
//   } //demo json
  
//   function restrictUser(userid, name, el) {
//     var els = $.trim($(el).text()); //trim any whitespace
//     console.log(els)
//     /*$.ajax({
//       url: '/restrict-user-ajax/' + userid,
//       dataType: 'json',
//       success: function(data) {*/
//     //check if status is true
//     if (data.status) {
//       //check previous text was block/unblock
//       if (els == "Block") {
//         //change text
//         $(el).text("Unblock")
//       } else {
//         $(el).text("Block")
//       }
//     }
//     /*}
//     });*/
  
  
//   }




// // $( document ).ready(function() {
// //     alert( "ready!" );
// // });

// let selection = document.querySelector('selected_Godown');
// // let result = document.querySelector('h2')
// selection.addEventListener('change',() => {
//   selection.innerText = selection.options[selection.selectedIndex].value;
// });


var e = document.getElementById("godownDropdown");
      function show(){
        var as = document.forms[0].godownDropdown.value;
        var strUser = e.options[e.selectedIndex].value;
        console.log(as, strUser);
      }
      e.onchange=show;
      show();