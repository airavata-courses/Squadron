package handlers

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestPreparePacket(t *testing.T){
	request := rainFallRequest{
		HouseArea: 100,
		PinCode:   47408,
		Months:    []string{"1", "2", "4"},
		RequestId: "test",
		Username:  "test-user",
	}
	require.NotNil(t, PreparePacket(request))
}
