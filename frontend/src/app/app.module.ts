import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { HeaderNavModule } from './header-nav/header-nav.module';
import { HomeModule } from './home/home.module';
import { AppRoutingModule } from './app.routes';

const routes: Routes = [];

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    RouterModule.forRoot(routes),
    BrowserModule,
    HeaderNavModule,
    HomeModule,
    AppRoutingModule
  ],
  exports: [
    RouterModule
  ],
  providers: [],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
