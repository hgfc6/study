package logic

import (
	"context"

	"golang/zero/internal/svc"
	"golang/zero/internal/types"

	"github.com/zeromicro/go-zero/core/logx"
)

type ZeroLogic struct {
	logx.Logger
	ctx    context.Context
	svcCtx *svc.ServiceContext
}

func NewZeroLogic(ctx context.Context, svcCtx *svc.ServiceContext) *ZeroLogic {
	return &ZeroLogic{
		Logger: logx.WithContext(ctx),
		ctx:    ctx,
		svcCtx: svcCtx,
	}
}

func (l *ZeroLogic) Zero(req *types.Request) (resp *types.Response, err error) {
	// todo: add your logic here and delete this line
	resp = new(types.Response)
	resp.Message = req.Name
	return
}
