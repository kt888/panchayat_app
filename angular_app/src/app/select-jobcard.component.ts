import { Component, OnInit } from '@angular/core';
import { AngularFire, FirebaseListObservable } from 'angularfire2'
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';


@Component({
    selector: 'select-jobcard',
    templateUrl: './select-jobcard.component.html'
    ,
    styleUrls: ['./app.component.css']
})

export class SelectJobcardComponent {
    title = "Select Jobcard";
    removeFromUrl = "panchayat/";

    items: FirebaseListObservable<any[]>

    constructor(private router: Router, private af: AngularFire) {
        var urlValue = this.router.url;
        var u = urlValue.replace(this.removeFromUrl, '');
	var base = '/jobcards'
	u = base.concat(u)
	console.log(u)
	
        this.items = af.database.list(u);
        var baseForJc = urlValue + '/jobcard';
        console.log(baseForJc)
    }

}
