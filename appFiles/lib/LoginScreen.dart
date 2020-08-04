import 'package:flutter/material.dart';
import 'package:loginandmainpage/main.dart';
import 'package:camera/camera.dart';

class LoginScreen extends StatefulWidget {
  final List<CameraDescription> cameras;
  final intMode;
  LoginScreen(this.cameras,this.intMode);

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  TextStyle style = TextStyle(fontFamily: 'Montserrat', fontSize: 20.0,fontStyle: FontStyle.italic);
  @override
  Widget build(BuildContext context) {
    final emailField= TextField(
      obscureText: false,
      style: style,
      decoration: InputDecoration(
          contentPadding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
          hintText: "Email",
          border: OutlineInputBorder(borderRadius: BorderRadius.circular(32.0))
      ),
    );
    final passwordField = TextField(
      obscureText: true,
      style: style,

      decoration: InputDecoration(
          fillColor: Colors.white,
          contentPadding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
          hintText: "Password",
          border:
          OutlineInputBorder(borderRadius: BorderRadius.circular(32.0))),
    );
    final loginButton= Material(
      elevation: 5.0,
      borderRadius: BorderRadius.circular(32.0),
      color: Colors.blue,
      child: MaterialButton(
        minWidth: MediaQuery.of(context).size.width,
        padding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
        onPressed:() {
          Navigator.pushNamed(context, '/cameraPage');
        },
        child: Text(
          'login',
          textAlign: TextAlign.center,
          style: style.copyWith(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );
    return Scaffold(
      body: Center(
        child: Container(

          color: Colors.tealAccent,
          child: Padding(
            padding: const EdgeInsets.all(36.0),

            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                SizedBox(
                    height: 155.0,
                    child: Image(
                      image: AssetImage('assets/loginPageDemo.jpeg'),
                      fit: BoxFit.fill,
                    )
                ),
                SizedBox(height: 45.0),
                Text(
                  'Emotion Detector',
                  style: TextStyle(
                    fontFamily: 'Pacifico',
                    fontWeight: FontWeight.bold,
                    fontSize: 25,
                  ),
                ),
                SizedBox(height: 45.0),
                emailField,
                SizedBox(height: 45.0),
                passwordField,
                SizedBox(height: 45.0,),
                loginButton,
                SizedBox(height: 15.0,)
              ],
            ),
          ),
        ),
      ),
    );
  }
}
