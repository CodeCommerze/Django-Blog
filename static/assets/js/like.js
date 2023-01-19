const like = document.getElementById('like-icon')
const count = document.getElementById('like-count')

like.onclick=()=>{
   const blogID = like.getAttribute('data-blog');
   url = `/blog_like/${blogID}`
   fetch(url,{
    method : "GET",
    headers :{
        'Content-Type': 'application/json'
    }

   })
   .then(res=> {
   return res.json()
   })
   .then((data)=>{
    if(data.liked){
        
        like.classList.remove('heart-color')
        like.classList.add('default-color')
    }
    else{
        like.classList.add('heart-color')
        like.classList.remove('default-color')
    }
    count.innerHTML = data.count;
   })
   .catch((err)=>{console.log(err)})

}