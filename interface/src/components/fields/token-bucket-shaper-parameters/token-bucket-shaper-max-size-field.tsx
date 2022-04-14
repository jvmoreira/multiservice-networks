import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketShaperParameterFieldProps } from './token-bucket-shaper-parameters';

export function TokenBucketShaperMaxSizeField(props: TokenBucketShaperParameterFieldProps): ReactElement {
  const { tokenBucketShaperParameters, setTokenBucketShaperParameters } = props;

  const tokenBucketShaperMaxSize = useMemo(() => {
    return tokenBucketShaperParameters.bucket_max_size || '';
  }, [tokenBucketShaperParameters]);

  const setTokenBucketShaperMaxSize = useSetNfvTeFunctionParameter('bucket_max_size', setTokenBucketShaperParameters);
  const onTokenBucketShaperMaxSizeChangeHandler = useChangeHandler(setTokenBucketShaperMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket"
      name="bucket-max-size"
      value={tokenBucketShaperMaxSize}
      placeholder="Valor em tokens"
      onChange={onTokenBucketShaperMaxSizeChangeHandler}
    />
  );
}
