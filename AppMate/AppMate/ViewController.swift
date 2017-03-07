//
//  ViewController.swift
//  AppMate
//
//  Created by HanYoungsoo on 2017. 3. 5..
//  Copyright © 2017년 YoungsooHan. All rights reserved.
//

import UIKit
import MapKit
import CoreLocation

class ViewController: UIViewController,CLLocationManagerDelegate, MKMapViewDelegate {

    @IBOutlet weak var mapView: MKMapView!
    
    let manager = CLLocationManager()

    let initialLocation = CLLocation(latitude: 37.3858128, longitude: 127.123164);
    let regionRadius: CLLocationDistance = 1000

    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        let locataion = locations.last
//        let span:MKCoordinateSpan = MKCoordinateSpanMake(0.01, 0.01)
//        let myLocation:CLLocationCoordinate2D = CLLocationCoordinate2DMake(locataion.coordinate.latitude+10, locataion.coordinate.longitude+10)
        let region:MKCoordinateRegion = MKCoordinateRegionMakeWithDistance(
            CLLocationCoordinate2DMake(locataion!.coordinate.latitude+0.01, locataion!.coordinate.longitude), 10000, 10000);
        
        mapView.setRegion(region, animated:true)
        self.mapView.showsUserLocation = true
//        self.manager.stopUpdatingLocation()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        manager.delegate = self
        manager.desiredAccuracy = kCLLocationAccuracyBest
        manager.requestWhenInUseAuthorization()
        manager.startUpdatingLocation()
        
        
        
        
//        centerMapOnLocation(location:initialLocation)
    
    }
    
    
    func centerMapOnLocation(location: CLLocation) {
        let coordinateRegion = MKCoordinateRegionMakeWithDistance(location.coordinate,
                                                                  regionRadius * 2.0, regionRadius * 2.0)
        mapView.setRegion(coordinateRegion, animated: true)
        
    }
    
    
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()

    }


}

