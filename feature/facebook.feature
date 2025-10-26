Feature: Facebook Login Automation
  As a user
  I want to automate Facebook login functionality
  So that I can test the login process efficiently

  Background:
    Given I am on the Facebook login page

  Scenario: Verify Facebook login page elements
    Then I should see the Facebook login form
    And I should see the email field
    And I should see the password field
    And I should see the login button
    And the page title should contain "Log into Facebook"

  Scenario: Navigate to forgot password page
    When I click on "Forgot account?" link
    Then I should be on page with URL containing "recover"

  Scenario: Navigate to sign up page
    When I click on "Sign up for Facebook" link
    Then I should be on page with URL containing "reg"

  Scenario: Attempt login with invalid credentials
    When I enter my email "invalid@example.com"
    And I enter my password "wrongpassword"
    And I click the login button
    Then I should see an error message

  Scenario: Login with valid credentials
    When I login with credentials from environment
    Then I should be redirected to Facebook home page

  @skip
  Scenario: Login with specific credentials
    When I enter my email "test@example.com"
    And I enter my password "testpassword"
    And I click the login button
    Then I should be redirected to Facebook home page