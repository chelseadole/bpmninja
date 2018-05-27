import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { QuizComponent } from './quiz.component';
import { QuestionComponent } from './question/question.component'

@NgModule({
  imports: [
    BrowserModule,
    CommonModule
  ],
  exports: [
    QuizComponent
  ],
  declarations: [
    QuizComponent,
    QuestionComponent
  ]
})

export class QuizModule { }
