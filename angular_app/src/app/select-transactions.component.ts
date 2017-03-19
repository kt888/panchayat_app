import { Component } from '@angular/core';
import { AngularFire, FirebaseListObservable, FirebaseObjectObservable } from 'angularfire2'
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';


@Component({
    selector: 'select-transactions',
    templateUrl: './select-transactions.component.html'
    ,
    styleUrls: ['./app.component.css']
})

export class SelectTransactionsComponent {
    title = "Select Transactions";

    items: FirebaseListObservable<any[]>

	jobcard_name = ""

    objects: FirebaseObjectObservable<any[]>;

    constructor(private router: Router, private af: AngularFire) {
        var urlValue = this.router.url;
        var jobcardId = urlValue.replace('/jobcard', '');
	var base = '/transactions'
	var path = base.concat(jobcardId);
	console.log(path);
        this.items = af.database.list(path);
	var string_list = jobcardId.split("/")
	this.jobcard_name = string_list[string_list.length - 1];
	console.log(this.jobcard_name);
	console.log("Printing");
	console.log(this.items);
    }

    selectedItem: any;
    onSelect(item): void {
        this.selectedItem = item;
    }
}
