require "test_helper"

class StaffListControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get staff_list_index_url
    assert_response :success
  end
end
