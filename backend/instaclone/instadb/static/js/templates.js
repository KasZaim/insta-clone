
function postsTemplate(i, post, commentsAmount) {
    return /*html*/`<div class="main-posts">
                <div class="post-header">
                    <div class="post-header-left">
                        <div class="profil-icon"><img src="${post['profilimg']}"></div>
                        <div class="influencer"><b>${post['user']}</b> ${post['location']}</div> 
                    </div>
                    <i class="fa-solid fa-ellipsis"></i>
                </div>
                
                <div class="post-img" id="carousel-container${i}">
                    ${post.image.length > 1 ? carouselTemplate(i, post): `<img id="multi-img${i}" src="${post.image[0]}" alt="Post image">`}   <!-- Mehrere Bilder -> Karussell anzeigen // Einzelnes Bild -->
                </div>

                <div class="interactions">
                    <div class="like-icons">
                        <div class="like-comment-share">
                            <img onclick="gotLiked(${i})" id="heart${i}" src="img/love.png" alt="">
                            <img src="img/comment.png">
                            <img src="img/send.png" alt="">
                        </div>
                        <div>
                            <b>Gefällt <span id="liked${i}"> ${post['likes']}</span> Mal</b>
                        </div>
                    </div>
                </div>
                <div id="posted-text-container${i}" class="post-text cut-posted-text">
                    <b>${post['user']}</b> ${post['description']} 
                    <span class="read-more" id="more${i}" onclick="readmore(${i})" >...more</span> 
                    <div id="full-text${i}" class="full-text d-none">
                        ${post['full-description']}
                    </div> 
                    <div class="hashtags">
                        ${post['hashtags']}
                    </div>
                </div>
                
                <div class="comments-amount">
                    Alle ${commentsAmount} Kommentare ansehen
                </div>
                <div class="comments" id="comments${i}">
                    
                </div>
                <div class="date">${post['date']}</div>
                
                <div class="comment-section">
                    <img src="img/smile.png" alt="">
                    <input id="comment-input${i}" onkeydown="enableButton(${i})" placeholder="Kommentieren ..." type="text">
                    <button disabled id="comment-btn${i}">Posten</button>
                </div>
            </div>`;
}


// function carouselTemplate(i, post) {
//     return/*html*/`<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
//                         <ol class="carousel-indicators">
//                             <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
//                             <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
//                             <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
//                         </ol>
//                         <div class="carousel-inner" id="carousel-inner">

//                         </div>
//                         <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
//                         <span class="carousel-control-prev-icon" aria-hidden="true"></span>
//                         <span class="sr-only">Previous</span>
//                         </a>
//                         <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
//                         <span class="carousel-control-next-icon" aria-hidden="true"></span>
//                         <span class="sr-only">Next</span>
//                         </a>
//                     </div>`;
// }

function carouselTemplate(i, post) {
    return /*html*/`
        <div id="carousel${i}" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
                ${post.image.map((_, index) => `
                    <button type="button" data-bs-target="#carousel${i}" data-bs-slide-to="${index}" 
                    class="${index === 0 ? 'active' : ''}" aria-current="true" aria-label="Slide ${index + 1}"></button>
                `).join('')}
            </div>
            <div class="carousel-inner">
                ${post.image.map((image, index) => `
                    <div class="carousel-item ${index === 0 ? 'active' : ''}">
                        <img src="${image}" class="d-block w-100" alt="...">
                    </div>
                `).join('')}
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carousel${i}" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carousel${i}" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>`;
}
