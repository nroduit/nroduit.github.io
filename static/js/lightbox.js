function isYoutubeLink(url) {
    const p = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
    return url.match(p);
}
function isImageLink(url) {
    const p = /([a-z\-_0-9\/:.]*\.(jpg|jpeg|png|gif))/i;
    return url.match(p);
}
function setGallery(el) {
    const elements = document.body.querySelectorAll(".gallery");
    elements.forEach(element => {
        element.classList.remove('gallery');
	});
	if(el.closest('ul, p')) {
        const link_elements = el.closest('ul, p').querySelectorAll("a[class*='lightbox-']");
        link_elements.forEach(link_element => {
			link_element.classList.remove('current');
		});
		link_elements.forEach(link_element => {
			if(el.getAttribute('href') === link_element.getAttribute('href')) {
				link_element.classList.add('current');
			}
		});
		if(link_elements.length>1) {
			document.getElementById('lightbox').classList.add('gallery');
			link_elements.forEach(link_element => {
				link_element.classList.add('gallery');
			});
		}
        let currentKey;
        const gallery_elements = document.querySelectorAll('a.gallery');
        Object.keys(gallery_elements).forEach(function (k) {
			if(gallery_elements[k].classList.contains('current')) currentKey = k;
		});

        let nextKey = parseInt(currentKey)+1;
        let prevKey = parseInt(currentKey)-1;
		if(nextKey>=(gallery_elements.length)) nextKey = gallery_elements.length-1;
		if(prevKey<0) prevKey = 0;

		document.getElementById('next').addEventListener("click", function() {
			gallery_elements[nextKey].click();
		});
		document.getElementById('prev').addEventListener("click", function() {
			gallery_elements[prevKey].click();
		});
	}
}

function setupLightbox() {
    const lightbox = document.getElementById('lightbox');
    lightbox.innerHTML = ''; // Clear existing content

    const closeLink = document.createElement('a');
    closeLink.id = 'close';
    lightbox.appendChild(closeLink);

    const nextLink = document.createElement('a');
    nextLink.id = 'next';
    nextLink.innerHTML = '&rsaquo;';
    lightbox.appendChild(nextLink);

    const prevLink = document.createElement('a');
    prevLink.id = 'prev';
    prevLink.innerHTML = '&lsaquo;';
    lightbox.appendChild(prevLink);

    lightbox.style.display = 'block';
}

function createImageLightbox(element) {
    setupLightbox();

    const lightbox = document.getElementById('lightbox');

    const imgDiv = document.createElement('div');
    imgDiv.classList.add('img');
    imgDiv.style.background = 'url(' + element.getAttribute('href') + ') center center / contain no-repeat';
    imgDiv.setAttribute('title', element.getAttribute('title'));

    const img = document.createElement('img');
    img.src = element.getAttribute('href');
    img.alt = element.getAttribute('title');
    imgDiv.appendChild(img);

    lightbox.appendChild(imgDiv);

    const span = document.createElement('span');
    span.textContent = element.getAttribute('title');
    lightbox.appendChild(span);

    setGallery(element);
}

function createYouTubeLightbox(element) {
    setupLightbox();

    const lightbox = document.getElementById('lightbox');

    const videoWrapperContainer = document.createElement('div');
    videoWrapperContainer.classList.add('videoWrapperContainer');

    const videoWrapper = document.createElement('div');
    videoWrapper.classList.add('videoWrapper');

    const iframe = document.createElement('iframe');
    iframe.setAttribute('src', `https://www.youtube.com/embed/${element.getAttribute('data-id')}?autoplay=1&showinfo=0&rel=0`);
    iframe.setAttribute('allowfullscreen', '');
    videoWrapper.appendChild(iframe);

    videoWrapperContainer.appendChild(videoWrapper);
    lightbox.appendChild(videoWrapperContainer);

    setGallery(element);
}

document.addEventListener("DOMContentLoaded", function() {

    //create lightbox div in the footer
    const newDiv = document.createElement("div");
    newDiv.setAttribute('id',"lightbox");
    document.body.appendChild(newDiv);

    //add classes to links to be able to initiate lightBoxes
    let elements = document.querySelectorAll('a');
    elements.forEach(element => {
        const url = element.getAttribute('href');
        if(url) {
            if(isYoutubeLink(url) && !element.classList.contains('no-lightbox')) {
                element.classList.add('lightbox-youtube');
                element.setAttribute('data-id',isYoutubeLink(url));
            }
            if(isImageLink(url) && !element.classList.contains('no-lightbox')) {
                element.classList.add('lightbox-image');
                // var href = element.getAttribute('href');
                // var filename = href.split('/').pop();
                // var split = filename.split(".");
                // var name = split[0];
                // element.setAttribute('title',name);
            }
        }
    });

    //remove the clicked lightbox
    document.getElementById('lightbox').addEventListener("click", function(event) {
        if(event.target.id !== 'next' && event.target.id !== 'prev'){
            this.innerHTML = '';
            document.getElementById('lightbox').style.display = 'none';
        }
    });

    // Event listener for lightbox images
    const imageElements = document.querySelectorAll('a.lightbox-image');
    imageElements.forEach(element => {
        element.addEventListener("click", function(event) {
            event.preventDefault();
            createImageLightbox(this);
        });
    });

    // Event listener for YouTube videos in lightbox
    const youtubeElements = document.querySelectorAll('a.lightbox-youtube');
    youtubeElements.forEach(element => {
        element.addEventListener("click", function(event) {
            event.preventDefault();
            createYouTubeLightbox(this);
        });
    });
});
