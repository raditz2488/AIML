//
//  Faces.swift
//  FDDemo
//
//  Created by Rohan Bhale on 15/05/21.
//

import UIKit
import Vision

extension UIImage {
    func detectFaces(completion: @escaping ([VNFaceObservation]?) -> ()) {
        guard let image = self.cgImage else {
            return completion(nil)
        }
        
        let detectFaceRectanglesRequest = VNDetectFaceRectanglesRequest()
        
        DispatchQueue.global().async {
            let requestHandler = VNImageRequestHandler(cgImage: image, orientation: self.cgImageOrientation)
            
            try? requestHandler.perform([detectFaceRectanglesRequest])
            
            guard let observations = detectFaceRectanglesRequest.results as? [VNFaceObservation] else {
                return completion(nil)
            }
            
            completion(observations)
        }
    }
}
