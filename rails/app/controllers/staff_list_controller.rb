class StaffListController < ApplicationController
  def index
    @staff = Staff.all
  end
end
