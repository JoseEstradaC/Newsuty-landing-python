import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title = 'Newsuty-Landing';
  rotado = false;
  clickEvent() {
    var x = document.getElementById('myTopnav');
    if (x == null)
      return;
    if (x.className === 'topnav') {
      x.className += ' responsive';
    } else {
      x.className = 'topnav';
    }
    var burger = document.getElementById('burger');
    if (burger == null)
      return;
    if (this.rotado) {
      burger.style.transform = 'rotate(0deg)';
      this.rotado = false;
    } else {
      burger.style.transform = 'rotate(90deg)';
      this.rotado = true;
    }
  }
}
