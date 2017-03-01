import { Component } from '@angular/core';
import { AngularFire, FirebaseListObservable } from 'angularfire2'
import { ActivatedRoute } from '@angular/router'
import { Location } from '@angular/common';


@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})

export class AppComponent {
    title = 'FIELD FRIENDLY NREGA DATA';
    items: FirebaseListObservable<any[]>;


}

