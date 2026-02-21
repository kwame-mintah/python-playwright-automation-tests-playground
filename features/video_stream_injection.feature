Feature: Use fake device for media stream

  Scenario Outline: Webcam video stream is injected with mock
    Given I am a user on <url>
    And I grant permission for the site to access my webcam
    Then I should be able to view the stream on the page
    Examples:
      | url                   |
      | http://localhost:3000 |
