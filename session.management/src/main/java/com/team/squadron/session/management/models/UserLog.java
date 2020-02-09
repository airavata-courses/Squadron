package com.team.squadron.session.management.models;

import org.springframework.data.annotation.Id;

import java.util.List;

public class UserLog {

    @Id
    String requestId;

    String userId;

    int pincode;

    List<Integer> months;

    float houseArea;

    float modelResult;

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
}
