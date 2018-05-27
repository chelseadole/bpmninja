import { Component, OnInit } from '@angular/core';

import { QuizService } from './quiz.service';

@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.css']
})
export class QuizComponent implements OnInit {

  this.songCount = 0;
  this.totalSongs = 10;
  this.played = [];

  this.initQuiz = false;

  constructor() { }

  ngOnInit() {
  }

  public startQuiz() {

     if (songCount === 0) {
        this.initQuiz = true;
     } else {
        this.initQuiz = false;
     }

  }

}
