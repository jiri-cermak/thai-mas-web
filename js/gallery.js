(function() {
    'use strict';

    const images = [
        { id: '142' }, { id: '149' }, { id: '156' }, { id: '164' },
        { id: '175' }, { id: '176' }, { id: '182' }, { id: '185' },
        { id: '189' }, { id: '192' }, { id: '209' }, { id: '215' },
        { id: '227' }, { id: '231' }, { id: '233' }, { id: '259' }
    ];

    const galleryGrid = document.getElementById('gallery-grid');
    if (!galleryGrid) return;

    images.forEach((image, index) => {
        const id = image.id;

        const galleryItem = document.createElement('div');
        galleryItem.className = 'gallery-item';

        const picture = document.createElement('picture');

        const sourceWebp = document.createElement('source');
        sourceWebp.srcset = 'gallery/thumbs/' + id + '_thumb.webp 300w, gallery/medium/' + id + '_medium.webp 800w, gallery/large/' + id + '_large.webp 1200w';
        sourceWebp.sizes = '(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw';
        sourceWebp.type = 'image/webp';

        const sourceJpeg = document.createElement('source');
        sourceJpeg.srcset = 'gallery/thumbs/' + id + '_thumb.jpg 300w, gallery/medium/' + id + '_medium.jpg 800w, gallery/large/' + id + '_large.jpg 1200w';
        sourceJpeg.sizes = '(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw';
        sourceJpeg.type = 'image/jpeg';

        const fallbackImg = document.createElement('img');
        fallbackImg.src = 'gallery/medium/' + id + '_medium.jpg';
        fallbackImg.alt = 'Fotografie ' + (index + 1);
        fallbackImg.loading = 'lazy';

        picture.appendChild(sourceWebp);
        picture.appendChild(sourceJpeg);
        picture.appendChild(fallbackImg);

        galleryItem.appendChild(picture);
        galleryGrid.appendChild(galleryItem);
    });
})();
