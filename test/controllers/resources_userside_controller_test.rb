require "test_helper"

class ResourcesUsersideControllerTest < ActionDispatch::IntegrationTest
  test "should get tips" do
    get resources_userside_tips_url
    assert_response :success
  end
end
