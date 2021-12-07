
    tags = document.querySelectorAll('.tag')
    tags.forEach( tag => {
        tag.onclick = function(){
            tag_title = this.innerText
            
            fetch(`/filter_by_tag/${tag_title}`)
                .then( res => res.json())
                .then(data => console.log(data))
        }
    })
