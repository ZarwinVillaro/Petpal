require "test_helper"

class AdoptPetsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get adopt_pets_index_url
    assert_response :success
  end

  test "should get adoptation_form" do
    get adopt_pets_adoptation_form_url
    assert_response :success
  end

  test "should get view_pet" do
    get adopt_pets_view_pet_url
    assert_response :success
  end
end
