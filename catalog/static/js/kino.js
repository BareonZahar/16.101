// // members/static/kino.js:
//     let comments = []
//
//                     // получаем два элемента формы
//     let a = document.getElementById('comment-add').onclick =  function() {
//
//
//         event.preventDefault();
//     // при нажатии кнопки происходит обновление страницы - что этого небыло пишем следующее
//     //     это происходит потому что кнопка внутри формы
//     //     preventDefault();
//         let commentName = document.getElementById('comment-name');
//         let commentBody = document.getElementById('comment-body');
//          // теперь получим значение  создаем новый массив в единственном числе
//         let comment = {
//             name : commentName.value,
//             body : commentBody.value,
//             time : Math.floor(Date.now()/1000)
//         }
//         console.log(comment)
//         commentName.value = '';
//         commentBody.value = '';
//         // добавить в комент
//         comment.push(comment);
//         // сохроним в локол стореж напишем функцию
//         saveComments();
//         //   функция показать коментарий
//         showComments();
//         loadComments();
//     }
//
//
//     function saveComments(){
//         localStorage.setItem('comments',JSON.stringify(comments))
//     }
//
//     function loadComments(){
//         if (loadComments.getItem('comments')) comments = JSON.parse(loadComments.getItem('comments'));
//         showComments();
//     }
//
//     function showComments(){
//         let commentField = document.getElementById('comment-field');
//         let out = '';
//         comments.forEach(function (item){
//             out += `<p class="text-right small"><em>${timeConverter(item.time)}</em></p>`;
//             out += `<p class="alert alert-primary">${item.name}</p>`;
//             out += `<p class="alert alert-success">${item.body}</p>`;
//         });
//         commentField.innerHTML = out;
//     }
//
//     function timeConverter(UNIX_timestamp){
//         var a = new Date(UNIX_timestamp * 1000);
//         var mouths = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
//         var year = a.getFullYear();
//         var mouth = mouths[a.getMonth()];
//         var date = a.getDate();
//         var hour =  a.getHours();
//         var min = a.getMinutes();
//         var sec = a.getSeconds();
//         var time = date + ' ' + mouth + ' ' + year + ' ' + hour + ':' + min + ':' +sec;
//         return time;
//     }

  // const menu = document.querySelector('.menu');
  // const menuToggle = document.querySelector('.menu-toggle');
  //
  // menuToggle.addEventListener('onclick', () => {
  //   menu.classList.toggle('open');
  // });
function f1() {
    $('#newcomment').modal('show');
}

let likesCount = 0;

function addLike() {
  likesCount++;
  updateLikesCount();
}

function removeLike() {
  if (likesCount > 0) {
    likesCount--;
    updateLikesCount();
  }
}

function updateLikesCount() {
  document.getElementById('likes-count').innerText = likesCount;
}