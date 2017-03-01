import { Component } from '@angular/core';
import { AngularFire, FirebaseListObservable } from 'angularfire2'
import { ActivatedRoute } from '@angular/router'
import { Location } from '@angular/common';


@Component({
    selector: 'select-panchayat',
    templateUrl: './select-panchayat.html',
    styleUrls: ['./app.component.css']
})

export class SelectPanchayatComponent {
    title = 'Select Panchayat';
    items: FirebaseListObservable<any[]>;

    constructor(private af: AngularFire, private location: Location) {
        this.items = af.database.list('/data');
    }
}
