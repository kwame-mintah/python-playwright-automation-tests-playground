Feature: Use fake device for media stream

  Scenario Outline: Webcam video stream is injected with mock
    Given I am a user on site <url>
    And I am able to request an image for prediction
    Then I should be able to see the prediction result
    Examples:
      | url                   |
      | http://localhost:8080/ |
