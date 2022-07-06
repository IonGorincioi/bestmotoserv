var image = document.getElementById('slideimages');
var images = [
  '../static/images/aboutpage_images/pic1.jpg',
  '../static/images/aboutpage_images/pic2.jpg',
  '../static/images/aboutpage_images/pic3.jpg',
  '../static/images/aboutpage_images/pic4.jpg',
  '../static/images/aboutpage_images/pic5.jpg'
];

setInterval(function () {
  let random = Math.floor(Math.random() * 5);
  image.src = images[random];
}, 5000);
