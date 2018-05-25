import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderNavComponent } from './header-nav.component'

@NgModule({
  imports: [
    BrowserModule,
    CommonModule
  ],
  exports: [
    HeaderNavComponent
  ],
  declarations: [
    HeaderNavComponent
  ]
})

export class HeaderNavModule { }
