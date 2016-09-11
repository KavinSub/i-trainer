var application = function(){
		var i = 0
		RobotUtils.onService(function(ALTactileGesture, ALTextToSpeech, ALAnimationPlayer) {
			console.log("Ready to play");

			

			// ALSpeechRecognition.subscribe("dialogue_key");
			// ALSpeechRecognition.unsubscribe("dialogue_key")
			// console.log("voice recognized");


			RobotUtils.subscribeToALMemoryEvent('ready', function(value) {
				console.log(value);
				if (value == 1) {
					ALTextToSpeech.say("you said hello");
				} else if (value == 4) {
					// ALBehaviorManager.runBehavior("<uid>/ani;ations/disco")
				}
				switch(value) {
					case 1:
							ALTextToSpeech.say("you said hello");
							break;
					case 2:
							ALTextToSpeech.say("you said work out");
							break;
					case 3:
							ALTextToSpeech.say("you said ready");
							break;
					default:
							console.log("nothing happens");
				}

				// ALBehaviorManager.runBehavior("<uid>/ani;ations/disco")

			});

			RobotUtils.subscribeToALMemoryEvent('LeftBumperPressed', function(value) {

			 if (value == "0") {
				 ALAnimationPlayer.run("animations/Stand/Gestures/Enthusiastic_5");
				 i = i + 1;
				 console.log(i);
				 ALTextToSpeech.say(i.toString());
				 if (i == 5) {
					 ALTextToSpeech.say("Tada! You are done!");
				 }
			 }

			});
    });
}
