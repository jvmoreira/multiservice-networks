import React, { ReactElement, useEffect } from 'react';
import { StateUpdater } from '@/commons/change-handler';
import { useNfvTeFunctionParameters } from '@/commons/nfv-te-values';
import { TokenBucketPolicerIntervalField } from './token-bucket-policer-interval-field';
import { TokenBucketPolicerBucketSizeField } from './token-bucket-policer-bucket-size-field';
import { TokenBucketPolicerMaxSizeField } from './token-bucket-policer-max-size-field';
import { TokenBucketPolicerRateField } from './token-bucket-policer-rate-field';

type TokenBucketPolicerParameters = {
  rate: string,
  bucket_size: string,
  bucket_max_size: string,
  interval: string,
};

export function TokenBucketPolicerParameters(): ReactElement {
  const [
    tokenBucketPolicerParameters,
    setTokenBucketPolicerParameters,
  ] = useNfvTeFunctionParameters<TokenBucketPolicerParameters>();

  useSetTokenBucketPolicerInitialParameters(setTokenBucketPolicerParameters);

  return (
    <>
      <TokenBucketPolicerBucketSizeField
        tokenBucketPolicerParameters={tokenBucketPolicerParameters}
        setTokenBucketPolicerParameters={setTokenBucketPolicerParameters}
      />

      <TokenBucketPolicerMaxSizeField
        tokenBucketPolicerParameters={tokenBucketPolicerParameters}
        setTokenBucketPolicerParameters={setTokenBucketPolicerParameters}
      />

      <TokenBucketPolicerIntervalField
        tokenBucketPolicerParameters={tokenBucketPolicerParameters}
        setTokenBucketPolicerParameters={setTokenBucketPolicerParameters}
      />

      <TokenBucketPolicerRateField
        tokenBucketPolicerParameters={tokenBucketPolicerParameters}
        setTokenBucketPolicerParameters={setTokenBucketPolicerParameters}
      />
    </>
  );
}

export interface TokenBucketPolicerParameterFieldProps {
  tokenBucketPolicerParameters: TokenBucketPolicerParameters,
  setTokenBucketPolicerParameters: StateUpdater<TokenBucketPolicerParameters>,
}

function useSetTokenBucketPolicerInitialParameters(
  setTokenBucketPolicerParameters: StateUpdater<TokenBucketPolicerParameters>,
): void {
  useEffect(() => {
    setTokenBucketPolicerParameters({
      rate: '',
      bucket_size: '',
      bucket_max_size: '',
      interval: '',
    });
  }, [setTokenBucketPolicerParameters]);
}
