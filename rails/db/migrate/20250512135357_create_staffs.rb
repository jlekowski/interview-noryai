class CreateStaffs < ActiveRecord::Migration[8.0]
  def change
    create_table :staffs do |t|
      t.string :name
      t.integer :location_id
      t.date :date_of_birth
      t.string :iban
      t.string :bic

      t.timestamps
    end
  end
end
