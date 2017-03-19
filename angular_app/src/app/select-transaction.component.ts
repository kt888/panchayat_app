import { Component } from '@angular/core';
import { AngularFire, FirebaseListObservable, FirebaseObjectObservable } from 'angularfire2'
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';


@Component({
    selector: 'select-transaction',
    templateUrl: './select-transaction.component.html'
    ,
    styleUrls: ['./app.component.css']
})

export class SelectTransactionComponent {
    title = "Transaction";

    item: FirebaseObjectObservable<any>

    objects: FirebaseObjectObservable<any[]>;

    constructor(private router: Router, private af: AngularFire) {
        var urlValue = this.router.url;
	var transactionId = urlValue.replace('/transaction', '');
	transactionId = transactionId.replace('%3A', ':')
	var jobcardId = transactionId.split(":")[0]
	var base = '/transactions'
	var path = base.concat(jobcardId);
	path = path.concat(transactionId)
	this.item = af.database.object(path);
	console.log(this.item);
    }

}
