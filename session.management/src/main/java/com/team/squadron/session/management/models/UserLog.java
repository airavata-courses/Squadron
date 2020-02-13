package com.team.squadron.session.management.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.springframework.data.annotation.Id;

import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
public class UserLog {

    @Id
    String request_id;

    String username;

    int pincode;

    List<Integer> months;

    float house_area;

    float model_result;

    float post_processed_result;

    TransactionStatus status;

    public String getRequest_id() {
        return request_id;
    }

    public void setRequest_id(String request_id) {
        this.request_id = request_id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public int getPincode() {
        return pincode;
    }

    public void setPincode(int pincode) {
        this.pincode = pincode;
    }

    public List<Integer> getMonths() {
        return months;
    }

    public void setMonths(List<Integer> months) {
        this.months = months;
    }

    public float getHouse_area() {
        return house_area;
    }

    public void setHouse_area(float house_area) {
        this.house_area = house_area;
    }

    public float getModel_result() {
        return model_result;
    }

    public void setModel_result(float model_result) {
        this.model_result = model_result;
    }

    public float getPost_processed_result() {
        return post_processed_result;
    }

    public void setPost_processed_result(float post_processed_result) {
        this.post_processed_result = post_processed_result;
    }

    public TransactionStatus getStatus() {
        return status;
    }

    public void setStatus(TransactionStatus status) {
        this.status = status;
    }
}
