package handler

import (
	"net/http"

	"github.com/zeromicro/go-zero/rest/httpx"
	"golang/zero/internal/logic"
	"golang/zero/internal/svc"
	"golang/zero/internal/types"
)

func ZeroHandler(svcCtx *svc.ServiceContext) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var req types.Request
		if err := httpx.Parse(r, &req); err != nil {
			httpx.ErrorCtx(r.Context(), w, err)
			return
		}

		l := logic.NewZeroLogic(r.Context(), svcCtx)
		resp, err := l.Zero(&req)
		if err != nil {
			httpx.ErrorCtx(r.Context(), w, err)
		} else {
			httpx.OkJsonCtx(r.Context(), w, resp)
		}
	}
}
