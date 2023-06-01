var year=new Date().getFullYear()
var yr=document.querySelector(".demo")
yr.textContent += year

let Index = 0;
Slides();

function Slides() {
  let i;
  let slides = document.getElementsByClassName("Slides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  Index++;
  if (Index > slides.length) {Index = 1}
  slides[Index-1].style.display = "block";
  setTimeout(Slides, 2000); // Change image every 2 seconds
}