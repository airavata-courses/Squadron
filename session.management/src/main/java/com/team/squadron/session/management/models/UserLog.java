package com.team.squadron.session.management.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.springframework.data.annotation.Id;

import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
public class UserLog {

    @Id
    @JsonProperty(value="RequestId")
    String requestId;

    String userId;

    @JsonProperty(value="PinCode")
    int pincode;

    @JsonProperty(value="Months")
    List<Integer> months;

    @JsonProperty(value="HouseArea")
    float houseArea;

    float modelResult;

    float post_processed;

    TransactionStatus status;

    public TransactionStatus getStatus() { return status; }

    public void setStatus(TransactionStatus status) { this.status = status; }
    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getRequestId() {
        return requestId;
    }

    public void setRequestId(String requestId) {
        this.requestId = requestId;
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

    public float getHouseArea() {
        return houseArea;
    }

    public void setHouseArea(float houseArea) {
        this.houseArea = houseArea;
    }

    public float getModelResult() {
        return modelResult;
    }

    public void setModelResult(float modelResult) {
        this.modelResult = modelResult;
    }

    public float getPost_processed() {
        return post_processed;
    }

    public void setPost_processed(float post_processed) {
        this.post_processed = post_processed;
    }
}
