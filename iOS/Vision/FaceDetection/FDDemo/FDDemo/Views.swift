//
//  Views.swift
//  FDDemo
//
//  Created by Rohan Bhale on 15/05/21.
//

import SwiftUI

struct TwoStateButton: View {
    private let text: String
    private let disabled: Bool
    
    private let background: Color
    private let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            HStack {
                Spacer()
                
                Text(text).font(.title).bold().foregroundColor(.white)
                
                Spacer()
            }.padding().background(background).cornerRadius(10)
        }.disabled(disabled)
    }
    
    init(text: String,
         disabled: Bool,
         background: Color = .blue,
         action: @escaping () -> Void) {
        self.text = text
        self.disabled = disabled
        self.background = disabled ? .gray : background
        self.action = action
    }
}

struct Main: View {
    private let image: UIImage
    private let text: String
    private let button: TwoStateButton
    
    var body: some View {
        VStack {
            Image(uiImage: image).resizable().aspectRatio(contentMode: .fit)
            
            Spacer()
            
            Text(text).font(.title).bold()
            
            Spacer()
            
            self.button
        }
    }
    
    init(image: UIImage, text: String, button: () -> TwoStateButton) {
        self.image = image
        self.text = text
        self.button = button()
    }
}
