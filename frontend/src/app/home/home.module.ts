import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home.component'

@NgModule({
  imports: [
    BrowserModule,
    CommonModule
  ],
  exports: [
    HomeComponent
  ],
  declarations: [
    HomeComponent
  ]
})

export class HomeModule { }
